data = """330,legal_desk,ds-101,REF_ID_NOT_FOUND,The required reference_id was not found in the request
331,legal_desk,ds-102,REF_ID_INVALID,failed The reference_id used in the request is invalid
332,legal_desk,ds-103,CONTENT_NOT_FOUND,failed The required content was not found in the request
333,legal_desk,ds-104,CONTENT_INVALID,failed The content used in the request is invalid
334,legal_desk,ds-105,FIRST_PARTY_NAME_NOT_FOUND,The required first_party_name was not found in the request
335,legal_desk,ds-106,FIRST_PARTY_NAME_INVALID,The first_party_name used in the request is invalid
336,legal_desk,ds-107,SECOND_PARTY_NAME_NOT_FOUND,The required second_party_name was not found in the request
337,legal_desk,ds-108,SECOND_PARTY_NAME_INVALID,The second_party_name used in the request is invalid
338,legal_desk,ds-109,DUTY_PAYER_PHONE_NUMBER_NOT_FOUND,The required duty_payer_phone_number was not found in the request
339,legal_desk,ds-110,DUTY_PAYER_PHONE_NUMBER_INVALID,The duty_payer_phone_number used in the request is invalid
340,legal_desk,ds-111,STREET_ADDRESS_NOT_FOUND,The required street_address was not found in the request
341,legal_desk,ds-112,STREET_ADDRESS_INVAID,The street_address used in the request is invalid
342,legal_desk,ds-113,LOCALITY_INVALID,The locality used in the request is invalid
343,legal_desk,ds-114,CITY_NOT_FOUND,The required city was not found in the request
344,legal_desk,ds-115,CITY_INVALID,The city used in the request is invalid
345,legal_desk,ds-116,STATE_NOT_FOUND,The required state was not found in the request
346,legal_desk,ds-117,STATE_INVALID,The state used in the request is invalid
347,legal_desk,ds-118,REF_ID_NOT_UNIQUE,The specified reference_id is not unique
348,legal_desk,ds-119,PINCODE_INVALID,The pincode used in the request is invalid
349,legal_desk,ds-120,COUNTRY_INVALID,The country used in the request is invalid
350,legal_desk,ds-121,STAMP_AMOUNT_NOT_FOUND,The required stamp_amount was not found in the request
351,legal_desk,ds-122,STAMP_AMOUNT_INVALID,The stamp_amount used in the request is invalid
352,legal_desk,ds-123,CONSIDERATION_AMOUNT_NOT_FOUND,The required consideration_amount was not found in the request
353,legal_desk,ds-124,CONSIDERATION_AMOUNT_INVALID,The consideration_amount used in the request is invalid
354,legal_desk,ds-125,STAMP_STATE_NOT_FOUND,The required stamp_state was not found in the request
355,legal_desk,ds-126,STAMP_STATE_INVALID,The stamp_state used in the request is invalid
356,legal_desk,ds-127,STAMP_DUTY_PAID_NOT_FOUND,The required stamp_duty_paid_by was not found in the request
357,legal_desk,ds-128,STAMP_DUTY_PAID_INVALID,The stamp_duty_paid_by used in the request is invalid
358,legal_desk,ds-129,ERROR275,none
359,legal_desk,ds-130,ERROR276,none
360,legal_desk,ds-131,DOCUMENT_CATEGORY_NOT_FOUND,The required document_category was not found in the request
361,legal_desk,ds-132,DOCUMENT_CATEGORY_INVALID,The document_category used in the request is invalid
362,legal_desk,ds-133,ERROR279, error
363,legal_desk,ds-134,DOCUMENT_REF_ID_INVALID,The document_reference_no used in the request is invalid
364,legal_desk,ds-135,DUTYPATER_ENTITY_TYPE_NOT_FOUND,The required duty_payer_entity_type was not found in the request
365,legal_desk,ds-136,DUTYPATER_ENTITY_TYPE_INVALID,The duty_payer_entity_type used in the request is invalid
366,legal_desk,ds-137,DUTYPATER_ID_TYPE_NOT_FOUND,The required duty_payer_id_type was not found in the request
367,legal_desk,ds-138,DUTYPATER_ID_TYPE_INVALID,The duty_payer_id_type used in the request is invalid
368,legal_desk,ds-139,DUTYPATER_ID_NUMBER_NOT_FOUND,The required duty_payer_id_number was not found in the request
369,legal_desk,ds-140,DUTYPATER_ID_NUMBER_INVALID,The duty_payer_id_number used in the request is invalid
370,legal_desk,ds-141,DUTYPATER_ID_CONTENT_NOT_FOUND,The required duty_payer_id_content was not found in the request
371,legal_desk,ds-142,DUTYPATER_ID_CONTENT_INVALID,The duty_payer_id_content used in the request is invalid
372,legal_desk,ds-143,SUB_REG_OFFICE_NOT_FOUND,The required sub_registrar_office was not found in the request
373,legal_desk,ds-144,SUB_REG_OFFICE_INVALID,The sub_registrar_office used in the request is invalid
374,legal_desk,ds-145,PROPERTY_AREA_NOT_FOUND,The required property_area was not found in the request
375,legal_desk,ds-146,PROPERTY_AREA_INVALID,The property_area used in the request is invalid
376,legal_desk,ds-147,PROPERTY_AREA_UNIT_NOT_FOUND,The required property_area_unit was not found in the request
377,legal_desk,ds-148,PROPERTY_AREA_UNIT_INVALID,The property_area_unit used in the request is invalid
378,legal_desk,ds-149,TRANSACTION_ID_NOT_FOUND,The required transaction_id was not found in the request
379,legal_desk,ds-150,TRANSACTION_ID_INVALID,The transaction_id and reference_id used in the request is invalid
380,legal_desk,ds-151,NO_MATCH_FOUND,The x-parse-application-id does not match the x-parse-rest-api-key
381,legal_desk,ds-152,STAMP_PAPER_ACCEPTED,Your stamp paper request is accepted We will process the same
382,legal_desk,ds-153,APP_ID_NOT_FOUND,The required x-parse-application-id was not found in the request
383,legal_desk,ds-154,API_KEY_NOT_FOUND,The required x-parse-rest-api-key was not found in the request"""

start = 331
data = data.split('\n')
newD = []

for d in data:
   line = str(start)
   line += d[3:]
   start += 1
   newD.append(line)

for d in newD:
    print d