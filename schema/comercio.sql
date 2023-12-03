
create schema if not exists comercio;

create table if not exists comercio.tickers_daily (
    ticker      varchar(8) not null,
    trading_day date not null,
    open        numeric(20,10) not null,
    high        numeric(20,10) not null,
    low         numeric(20,10) not null,
    close       numeric(20,10) not null,
    volume      int not null,
    primary key( ticker, trading_day )
    );

drop index if exists comercio."idx_comercio_tickers_daily_ticker";
create index idx_comercio_tickers_daily_ticker on comercio.tickers_daily (
        ticker
    );
