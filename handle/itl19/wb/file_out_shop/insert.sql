
                            INSERT INTO `itl_finance_bill` 
                            (`gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                            `start_day`, `end_day`, `ought_amount`, `real_amount`, `discount_amount`, `round_amount`, 
                            `owe_amount`, `estate_type`, `estate_id`, `debtor_card_type`, `debtor_card_no`, `debtor_name`, 
                            `debtor_mobile`, `zone_subject_id`) 
                            SELECT `gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                            `start_day`, `end_day`, 200.00, 0, 0, 0, 
                            200.00, `estate_type`, `estate_id`, `debtor_card_type`, `debtor_card_no`, `debtor_name`, 
                            `debtor_mobile`, `zone_subject_id` FROM itl_finance_bill WHERE id = 417791;
                          

                            INSERT INTO `itl_finance_bill` 
                            (`gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                            `start_day`, `end_day`, `ought_amount`, `real_amount`, `discount_amount`, `round_amount`, 
                            `owe_amount`, `estate_type`, `estate_id`, `debtor_card_type`, `debtor_card_no`, `debtor_name`, 
                            `debtor_mobile`, `zone_subject_id`) 
                            SELECT `gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                            `start_day`, `end_day`, 300.00, 0, 0, 0, 
                            300.00, `estate_type`, `estate_id`, `debtor_card_type`, `debtor_card_no`, `debtor_name`, 
                            `debtor_mobile`, `zone_subject_id` FROM itl_finance_bill WHERE id = 418032;
                          

                            INSERT INTO `itl_finance_bill` 
                            (`gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                            `start_day`, `end_day`, `ought_amount`, `real_amount`, `discount_amount`, `round_amount`, 
                            `owe_amount`, `estate_type`, `estate_id`, `debtor_card_type`, `debtor_card_no`, `debtor_name`, 
                            `debtor_mobile`, `zone_subject_id`) 
                            SELECT `gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                            `start_day`, `end_day`, 180.00, 0, 0, 0, 
                            180.00, `estate_type`, `estate_id`, `debtor_card_type`, `debtor_card_no`, `debtor_name`, 
                            `debtor_mobile`, `zone_subject_id` FROM itl_finance_bill WHERE id = 418523;
                          
