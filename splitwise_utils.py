import os
from splitwise import Splitwise
from splitwise.expense import Expense, ExpenseUser

class SplitwiseManager:
    def __init__(self, consumer_key, consumer_secret, access_token=None):
        """
        Initialize the Splitwise manager with consumer key and secret.
        If you already have an access token (after OAuth), you can pass it directly.
        Otherwise, we need to perform OAuth flow to obtain it.
        """
        self.s = Splitwise(consumer_key, consumer_secret)
        
        if access_token:
            # If we already have a stored token
            self.s.setOAuth2AccessToken(access_token)
        else:
            # handle the OAUTH flow here
            pass

    def create_expense(self, cost, description, group_id, user_shares):
        """
        Create an expense in a specified group with cost, description, and user share assignments.

        user_shares is a list of dictionaries:
        [
          { 'user_id': <splitwise-user-id>, 'paid_share': <amount_paid>, 'owed_share': <amount_owed> },
          ...
        ]
        Typically, only 1 user might have 'paid_share' = cost, others 0. 
        The 'owed_share' split can be distributed among the group.
        """
        expense = Expense()
        expense.setCost(cost)
        expense.setDescription(description)
        expense.setGroupId(group_id)
        
        expense_users = []
        for share in user_shares:
            eu = ExpenseUser()
            eu.setId(share["user_id"])       
            eu.setPaidShare(str(share["paid_share"]))
            eu.setOwedShare(str(share["owed_share"]))
            expense_users.append(eu)

        expense.setUsers(expense_users)
        created_expense = self.s.createExpense(expense)
        return created_expense

    def get_group_expenses(self, group_id, limit=0):
        """
        Return the list of expenses in the given group.
        If limit=0, it fetches all. Otherwise, fetches up to `limit`.
        """
        expenses = self.s.getExpenses(group_id=group_id, limit=limit)
        return expenses

    def get_monthly_report(self, group_id, year, month):
        """
        Return a basic monthly report for a group by filtering 
        the expenses within the specified year/month.
        """
        expenses = self.s.getExpenses(group_id=group_id)
        month_str = f"{year}-{month:02d}"
        
        monthly_expenses = []
        for exp in expenses:
            # expense_date might be something like "2025-02-19T13:25:00Z"
            # or "2025-02-19"
            if exp.getDate().startswith(month_str):
                monthly_expenses.append(exp)

        total_cost = sum(float(e.getCost()) for e in monthly_expenses)
        return monthly_expenses, total_cost
