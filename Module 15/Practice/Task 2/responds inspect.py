import json


errors_in_file = []
with open('shop respond.json', 'r', encoding='utf8') as respondsFile:
    respondsList = json.load(respondsFile)

for respond in respondsList:
    issue_report = {}
    for parameter in respond:
        if parameter == 'remoteHost' or parameter == 'partyId' or parameter == 'sessionId' or\
                parameter == 'pageViewId' or parameter == 'item_id' or parameter == 'basket_price' or\
                parameter == 'userAgentName' or parameter == 'referer' or parameter == 'location' or \
                parameter == 'item_url' or parameter == 'eventType':

            if not type(respond[parameter]) == str:
                issue_report['timestamp_of_issued_respond'] = respond['timestamp']
                issue_report[parameter] = f"'{str(respond[parameter])}' (must be string)"
            else:
                if parameter == 'referer' or parameter == 'location' or parameter == 'item_url':
                    if not (respond[parameter][:7] == r'https://' or respond[parameter][:8] == r'https://'):
                        issue_report['timestamp_of_issued_respond'] = respond['timestamp']
                        issue_report[parameter] = f"'{str(respond[parameter])}' " \
                                                  f"(must begin with https://' or 'https://')"

                elif parameter == 'eventType':
                    if not (respond[parameter] == 'itemBuyEvent' or respond[parameter] == 'itemViewEvent'):
                        issue_report['timestamp_of_issued_respond'] = respond['timestamp']
                        issue_report[parameter] = f"'{str(respond[parameter])}' " \
                                                  f"(must be 'itemBuyEvent' or 'itemViewEvent')"

        elif parameter == 'timestamp' or parameter == 'item_price':
            if not type(respond[parameter]) == int:
                issue_report['timestamp_of_issued_respond'] = respond['timestamp']
                issue_report[parameter] = f"'{str(respond[parameter])}' must be int"
        else:
            if not type(respond[parameter]) == bool:
                issue_report['timestamp_of_issued_respond'] = respond['timestamp']
                issue_report[parameter] = f"'{str(respond[parameter])}' must be bool"

    if len(issue_report) >= 1:
        errors_in_file.append(issue_report)


if errors_in_file:
    with open('test results.json', 'w') as testResults:
        json.dump(errors_in_file, testResults, indent=4)
    print("Fail\nTest results can be viewed in 'test results.json'")
else:
    print("Pass")