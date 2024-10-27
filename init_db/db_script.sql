CREATE TABLE Accounts (
    account_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    balance_end_day DECIMAL(15, 2) NOT NULL DEFAULT 0
);

CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,
    account_id UUID REFERENCES Accounts(account_id),
    amount DECIMAL(15, 2) NOT NULL CHECK (amount > 0),
    transaction_datetime TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    operation VARCHAR(10) CHECK (operation IN ('deposit', 'transfer', 'withdraw')) NOT NULL,
    cash_flow VARCHAR(10) CHECK (cash_flow IN ('cash_in', 'cash_out')) NOT NULL,
    reference_id UUID,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_account_id ON Transactions (account_id);
CREATE INDEX idx_reference_id ON Transactions (reference_id);