CREATE TABLE Accounts (
    account_uuid UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    balance DECIMAL(15, 2) NOT NULL CHECK (balance >= 0)
);

CREATE TABLE Transactions (
    transaction_uuid UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    beneficiary_account UUID REFERENCES Accounts(account_uuid),
    amount DECIMAL(15, 2) NOT NULL CHECK (amount > 0),
    cash_flow VARCHAR(10) CHECK (cash_flow IN ('cash_in', 'cash_out')) NOT NULL,
    operation VARCHAR(10) CHECK (operation IN ('deposit', 'transfer', 'withdraw')) NOT NULL,
    transaction_timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    origin_account UUID REFERENCES Accounts(account_uuid),
    description TEXT
);

CREATE INDEX idx_beneficiary_account ON Transactions (beneficiary_account);
CREATE INDEX idx_origin_account ON Transactions (origin_account);