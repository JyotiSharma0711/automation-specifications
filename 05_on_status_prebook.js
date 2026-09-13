/**
 * Validates the incoming request payload for an API call in the transaction flow.
 * 
 * @param {Object} targetPayload - The incoming request payload to validate.
 * @param {Object} sessionData - Data collected from previous transaction steps.
 * 
 * @returns {Object} { valid: boolean, code: number, description: string }
 */
function validate(targetPayload, sessionData) {

  if (!targetPayload?.context) {
    return { valid: false, code: 400, description: "Missing context in payload" };
  }

  if (targetPayload.context.action !== "on_status") {
    return { valid: false, code: 400, description: "Invalid action in context" };
  }

  if (!targetPayload?.message?.order) {
    return { valid: false, code: 400, description: "Missing message.order in payload" };
  }

  const order = targetPayload.message.order;

  if (!order.provider?.id) {
    return { valid: false, code: 400, description: "Missing provider.id in payload" };
  }

  if (!Array.isArray(order.items) || order.items.length === 0) {
    return { valid: false, code: 400, description: "Missing items in payload" };
  }

  const item = order.items[0];

  if (!item.id) {
    return { valid: false, code: 400, description: "Missing items[0].id in payload" };
  }

  if (!order.quote?.id) {
    return { valid: false, code: 400, description: "Missing quote.id in payload" };
  }

  const expectedItem = sessionData?.item?.[0];
  // The submission_id lives in sessionData.selected_items_xinput (carried forward by every
  // on_status generate() step) - NOT on sessionData.item, whose xinput only ever holds the
  // eKYC form to fill, never the filled-in form_response.
  const expectedSubmissionId = sessionData?.selected_items_xinput?.[0]?.form_response?.submission_id;

  const mismatch = matchAgainstEarlierCalls(order, item, expectedItem, expectedSubmissionId, sessionData);
  if (mismatch) {
    return { valid: false, code: 400, description: mismatch };
  }

  return { valid: true, code: 200, description: "Valid request" };
}

/**
 * Cross-checks provider/item/category/fulfillment/quote/submission_id on an order against
 * what earlier calls in this transaction established. Returns a description of the first
 * mismatch found, or null when everything there is a prior value for lines up.
 */
function matchAgainstEarlierCalls(order, item, expectedItem, expectedSubmissionId, sessionData) {
  return (
    fieldMismatch("order.provider.id", order.provider.id, sessionData?.selected_provider?.[0]?.id, "the provider selected earlier") ||
    fieldMismatch("order.items[0].id", item.id, expectedItem?.id, "the item selected earlier") ||
    arrayMismatch("category_id", item.category_ids, expectedItem?.category_ids, "the item selected earlier") ||
    arrayMismatch("fulfillment_id", item.fulfillment_ids, expectedItem?.fulfillment_ids, "the item selected earlier") ||
    fieldMismatch("order.quote.id", order.quote.id, sessionData?.quote_id?.[0], "the quote issued earlier") ||
    fieldMismatch("xinput.form_response.submission_id", item.xinput?.form_response?.submission_id, expectedSubmissionId, "the earlier callback")
  );
}

/**
 * Returns a mismatch description when both `actual` and `expected` are present and differ,
 * otherwise null (nothing to compare against yet, or values agree).
 */
function fieldMismatch(label, actual, expected, source) {
  if (expected && actual && actual !== expected) {
    return `${label} "${actual}" does not match ${source} ("${expected}")`;
  }
  return null;
}

/**
 * Returns a mismatch description for the first entry of `actual` missing from `expected`,
 * when both are arrays; otherwise null.
 */
function arrayMismatch(label, actual, expected, source) {
  if (Array.isArray(actual) && Array.isArray(expected)) {
    const bad = actual.find((id) => !expected.includes(id));
    if (bad) return `${label} "${bad}" does not match ${source}`;
  }
  return null;
}
