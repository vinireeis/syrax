from psycopg.sql import SQL

insert_new_account_query = SQL(
    obj="INSERT INTO Accounts (account_id, balance) VALUES (%(account_id)s, %(balance)s)"
)

list_all_accounts_query = SQL(obj="SELECT * FROM Accounts")

insert_one_transaction_query = SQL(
    obj="""
                INSERT INTO Transactions (account_id, amount, operation, cash_flow, reference_id) 
                VALUES (%(account_id)s, %(amount)s, %(operation)s, %(cash_flow)s, %(reference_id)s)
                    """
)

get_transactions_by_account_query = SQL(
    obj="SELECT * FROM Transactions WHERE account_id = %(account_id)s"
)

balance_query_lock = SQL(
    """ SELECT balance FROM Accounts WHERE account_id = %(account_id)s FOR UPDATE """
)

amount_deposit_query_update = SQL(
    """ 
            UPDATE Accounts SET balance = balance + %(amount)s WHERE account_id = %(account_id)s
            """
)

target_account_balance_query_lock = SQL(
    """ SELECT balance FROM Accounts WHERE account_id = %(target_account_id)s FOR UPDATE """
)

cash_out_query_update = SQL(
    """ 
                        UPDATE Accounts SET balance = balance - %(amount)s WHERE account_id = %(account_id)s
                        AND balance - %(amount)s >= 0
                        """
)
