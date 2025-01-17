# -*- coding: utf-8 -*-
"""
@Name:        GenClass.py
@Describe:    XXX
@Time:        2025/01/17 10:19:10
@Author:      Ray
@Version:     1.0
"""


def main():
    class_1 = {
        "予算管理": ["Budget Analysis", "Budget Consumption Report", "Budget Entry Document 360° View", "Budget Line Item Analyzer", "Budget Period Group 360° View", "Budget Period: Maintain, Manage Budget Periods - 360° View", "Budget Report", "Budget Version Comparison", "Budget View by Document Type", "Budgeting Workbench, Budgeting Workbench - Create Budget Document", "Manage Budget Periods", "Manage Budget Structure Elements", "Manage Budget Transfers", "Overview of AVC Data", "Period Budget and Commitment/Actual Line Item Analyzer"],
        "実行制御": ["Commitment Line Item Analyzer", "Commitments and Actuals Analyses", "Commitments and Funds Transfers", "Controlling Line Item Analyzer", "Display Funds Commitment", "Display Funds Precommitment", "Display Funds Reservation", "Display Funds Transfer", "Manage Commitment Items", "Availability Control Line Item Analyzer", "Personalization for Annual AVC Apps", "Personalization for Overall AVC Apps", "Overview of AVC Data"],
        "予算支出": ["Display Fund", "Display Fund Group", "Display Funds Block", "Display Funds Center Group", "Display Funds Center in FM Area", "Fund Group 360° View", "Funded Program Group 360° View", "Funded Program: Display", "Grant 360° View", "Grant Group 360° View", "Manage Applications of Funds", "Manage Funded Programs", "Manage Funds", "Manage Funds Centers"],
        "分析モニタリング": ["Actual Line Item Analyzer", "Drilldown for Budget Entry Documents", "FM Line Item Browser", "FM: Functional Area", "Fiscal Year Change Monitor", "Functional Area Group 360° View", "Display Forecast of Revenue", "Display Functional Area Group", "Display Hierarchy Variant/Funds Ctr", "Display Grant", "Display Grant Group", "Display Commitment Item Group", "Display Commitment Item: Hierarchy", "Display Grant Group", "Display Functional Area Group", "Funds Center Group 360° View", "Manage Global Hierarchies"],
        "会計財務": ["FI Postings", "CO Postings", "All Postings", "Display Entry Document", "Display Budget Documents", "Display Posting Addresses", "Display Clearing Request""Release Acceptance Request", "Release Clearing Request", "Release Payment Request", "Release Standing Request", "Earmarked Funds: Approval"],
    }

    list_1 = ["Actual Line Item Analyzer", "All Postings", "Availability Control Line Item Analyzer", "Budget Analysis", "Budget Consumption Report", "Budget Entry Document 360° View", "Budget Line Item Analyzer", "Budget Period Group 360° View", "Budget Period: Maintain, Manage Budget Periods - 360° View", "Budget Report", "Budget Version Comparison", "Budget View by Document Type", "Budget and Commitment/Actual line Item analyzer", "Budgeting Workbench, Budgeting Workbench - Create Budget Document", "CO Postings", "Commitment Item Group 360° View", "Commitment Line Item Analyzer", "Commitments and Actuals Analyses", "Commitments and Funds Transfers", "Controlling Line Item Analyzer", "Display Acceptance Request", "Display Application of Funds", "Display Budget Addresses", "Display Budget Documents", "Display Budget Period Group", "Display Clearing Request", "Display Commitment Item Group", "Display Commitment Item: Hierarchy", "Display Earmarked Funds", "Display Entry Document", "Display FM Document", "Display Forecast of Revenue", "Display Functional Area Group", "Display Fund", "Display Fund Group", "Display Funded Program Group", "Display Funds Block", "Display Funds Center Group", "Display Funds Center in FM Area", "Display Funds Commitment", "Display Funds Precommitment",
              "Display Funds Reservation", "Display Funds Transfer", "Display Grant", "Display Grant", "Display Grant Group", "Display Hierarchy Variant/Funds Ctr", "Display Payment Request", "Display Posting Addresses", "Display Standing Request", "Display commitment item", "Drilldown for Budget Entry Documents", "Earmarked Funds Document 360° View", "Earmarked Funds Journal", "Earmarked Funds: Approval", "FI Postings", "FM Line Item Browser", "FM Line Item Browser", "FM: Functional Area", "Fiscal Year Change Monitor", "Functional Area Group 360° View", "Fund Group 360° View", "Funded Program Group 360° View", "Funded Program: Display", "Funds Center Group 360° View", "Grant 360° View", "Grant Group 360° View", "Manage Applications of Funds", "Manage Budget Periods", "Manage Budget Structure Elements", "Manage Budget Transfers", "Manage Commitment Items", "Manage Earmarked Funds", "Manage Functional Areas", "Manage Funded Programs", "Manage Funds", "Manage Funds Centers", "Manage Global Hierarchies", "My Budget Alerts", "My Budget Overview", "Overview of AVC Data", "Period Budget and Commitment/Actual Line Item Analyzer", "Personalization for Annual AVC Apps", "Personalization for Overall AVC Apps", "Release Acceptance Request", "Release Clearing Request", "Release Payment Request", "Release Standing Request"]

    for item in list_1:
        flag = True
        for key, value in class_1.items():
            if item in value:
                flag = False
                print(key)
                break
        if flag:
            print("その他の機能")

    print(len(list_1))


if __name__ == '__main__':
    main()
