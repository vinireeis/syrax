CREATE TABLE Accounts (
    account_id UUID PRIMARY KEY,
    balance DECIMAL(15, 2) NOT NULL DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
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

INSERT INTO ACCOUNTS (account_id) values ('46f793c8-78ad-48ce-98ab-1aa09b5cc0d2');
INSERT INTO ACCOUNTS (account_id) values ('84123974-58c1-44b8-a69a-c9086d87e765');
INSERT INTO ACCOUNTS (account_id) values ('4dd6889d-cf50-43a9-a0bd-bec0582f7483');

CREATE INDEX idx_account_id ON Transactions (account_id);
CREATE INDEX idx_reference_id ON Transactions (reference_id);