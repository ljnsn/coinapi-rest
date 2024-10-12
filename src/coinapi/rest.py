"""SDK."""

from collections.abc import Callable

import httpx

from coinapi import utils
from coinapi._hooks import SDKHooks
from coinapi.config import CoinAPIConfig
from coinapi.exchange_rates import ExchangeRates
from coinapi.indexes import Indexes
from coinapi.metadata import Metadata
from coinapi.metrics import Metrics
from coinapi.models import components
from coinapi.ohlcv import Ohlcv
from coinapi.order_book import OrderBook
from coinapi.order_book_l3 import OrderBookL3
from coinapi.quotes import Quotes
from coinapi.trades import Trades

# ruff: noqa: E501


class CoinAPI:
    r"""REST API!

    RESTful endpoint provides the widest range of data, based on HTTP protocol which works in Request-Reply scheme.

    Implemented Standards:

     * [HTTP1.0](https://datatracker.ietf.org/doc/html/rfc1945)
     * [HTTP1.1](https://datatracker.ietf.org/doc/html/rfc2616)
     * [HTTP2.0](https://datatracker.ietf.org/doc/html/rfc7540)
     * [OpenAPI v3](https://www.openapis.org/)

    > **Note:** We adhere to the OpenAPI standards for documenting our API.

    ## OpenAPI Specification

    To access our API's OpenAPI specification, you can use the following link: [OpenAPI v3](https://raw.githubusercontent.com/coinapi/coinapi-sdk/master/data-api/coinapi-marketdata-rest.yaml)

    If you need to import the OpenAPI file into software like Postman, simply copy and paste the link below:
    ```shell
    https://raw.githubusercontent.com/coinapi/coinapi-sdk/master/data-api/coinapi-marketdata-rest.yaml
    ```

    ## Endpoints

    Enviroment | Encryption | Value
    --- | --- | ---
    Production | Yes | `https://rest.coinapi.io/`
    Production | No | `http://rest.coinapi.io/`

    :::info

    For real-time market data streaming, you should use WebSockets. REST API only supports pooling, meaning you can periodically request the current market data state. In streaming, you subscribe and data or updates are delivered to you continuously.

    :::

    ## General

    If you want to learn how to authenticate to this API, you can find detailed instructions and guidance in
    [authentication section](/authentication) of this documentation.

    ### HTTP Requests

    Each HTTP request must contain the header ``Accept: application/json`` as all our responses are in JSON format.

    We encourage you to use the HTTP request header ``Accept-Encoding: deflate, gzip`` for all requests.
    This will indicate to us that we can deliver compressed data to you which on your side should be decompressed transparently.

    :::tip

    By allowing data compression you are lowering bandwidth requirements by approximately 80%.
    This is important for requesting large amounts of data or using WebSocket Streaming API,
    as we can deliver data to you faster and more effectively.

    :::

    #### HTTP Success

    Successful HTTP responses have the status code `200` and the body in a format according to documentation of the requested resource.

    :::info

    You should always check that your HTTP response status code is equal to 200, otherwise the requested was not successful.

    :::

    #### HTTP Errors

    > Error message is returned in JSON structured like this:

    ```json
    {
        \"error\": \"Invalid API key\"
    }
    ```

    All HTTP requests with response status codes different to `200` must be considered as failed
    and you should expect additional JSON inside the body of the response with the error message encapsulated inside it as shown in the example.
    We use the following error codes:

    Error Code | Meaning
    ---------- | -------
    400 | Bad Request -- There is something wrong with your request
    401 | Unauthorized -- Your API key is wrong
    403 | Forbidden -- Your API key doesnt't have enough privileges to access this resource
    429 | Too many requests -- You have exceeded your API key rate limits
    550 | No data -- You requested specific single item that we don't have at this moment.

    :::info

    Good practice is to store all error messages somewhere along with request data for further manual review.

    :::

    ### Limits

    Any authenticated endpoint is providing (in HTTP response headers) information about the current state of the limits associated with API Key. In this section we will describe each limit.

    #### Request limit / APIKey

    ```html
    X-RateLimit-Limit: 1000000
    X-RateLimit-Remaining: 999989
    X-RateLimit-Request-Cost: 1
    ```

    The request limit define number of maximum requests that could be executed in the 24 hours period (sliding/rollowing window - always last 24 hours from specific moment) for your subscription.

    We define request as data request credits and this is not always equal to the number of API calls executed against the API. A request is deemed to be a single one if the limit query parameter on the endpoint isn’t available, isn’t used or it's stated otherwise in the API documentation. Otherwise — if the limit query parameter is available and is used — then each of the 100 data points returned in the response is counted as one request.

    For example at the 2019-08-22 13:00 UTC value of the requests remaining (X-RateLimit-Remaining) will be equal to the allocated quota (X-RateLimit-Limit) decreased by the sum of the request costs (SUM(X-RateLimit-Request-Cost)) executed in the period 2019-08-21 13:00 UTC - 2019-08-22 13:00 UTC (last 24 hours).


    HTTP Header | Type | Description
    ---------- | ------- | ---
    X-RateLimit-Used | int | Provides information about the request limit that has been used within the last 24-hour period. This header indicates the amount of request capacity consumed based on the usage history. It is important to note that the header is not always appended to every request to optimize the operation of the API.
    X-RateLimit-Limit | int | Is an optional feature that can be enabled via the customer portal to impose a limit on the capabilities of a specific API key. It allows you to define a threshold for the number of requests that can be made using a single API key within a 24-hour time frame.
    X-RateLimit-Remaining | int | Provides information about the number of requests that can still be made within the last 24-hour period based on the usage history. This header serves as a helpful indicator of the remaining request capacity, allowing API consumers to manage their usage effectively. It is important to note that the header is not always appended to every request to optimize the operation of the API.
    X-RateLimit-Request-Cost | int | The number of requests used to generate current HTTP response.
    X-RateLimit-Quota-Overage | string | Provides information about whether a given API key may exceed the plan quota within a 24-hour time frame, which could result in additional charges. This header is fully defined and configured in the customer portal.
    X-RateLimit-Quota-Allocated | string |  Total number of requests that can be made within a specific subscription during a 24-hour time frame. This quota allocation is determined based on the user's subscription purchase.
    X-RateLimit-Quota-Remaining | string | Provides valuable information about the remaining quota within the subscription for making requests within a 24-hour time frame. This header indicates the number of requests that can still be made within the allocated quota for the current 24-hour period.

    ```json
    GET v1/exchanges/ECB/apiKey-ED802AF4-E855-YOUR-API-KEY
    Host: coinapi.io
    X-RateLimit-Used: 1000
    X-RateLimit-Limit: 5000
    X-RateLimit-Remaining: 4000
    X-RateLimit-Request-Cost: 1
    X-RateLimit-Quota-Overage: ENABLED
    X-RateLimit-Quota-Allocated: 10000
    X-RateLimit-Quota-Remaining: 5000
    ```

    Explanation:

    - X-RateLimit-Used: 1000 (requests used in the last 24 hours)
    - X-RateLimit-Limit: 5000 (total request limit within a 24-hour time frame)
    - X-RateLimit-Remaining: 4000 (requests remaining within the last 24 hours)
    - X-RateLimit-Request-Cost: 1 (cost or \"weight\" of each individual request)
    - X-RateLimit-Overage: ENABLED (API key may exceed the plan quota within a 24-hour time frame)
    - X-RateLimit-Quota-Allocated: 10000 (total number of requests allowed for all API keys within the subscription within a 24-hour time frame)
    - X-RateLimit-Quota-Remaining: 5000 (requests remaining within the subscription's allocated quota within the last 24 hours)

    #### Concurrency limit / APIKey

    ```html
    X-ConcurrencyLimit-Limit: 10
    X-ConcurrencyLimit-Remaining: 5
    ```

    The concurrency limit defines the number of maximum concurrent API calls/requests that the API could process for your subscription at the current moment. Every API call/request increases the Concurrency limit against quota, and when it finishes, decreases it.

    HTTP Header | Type | Description
    ---------- | ------- | ---
    X-ConcurrencyLimit-Limit | int | Concurrency limit allocated for your API key.
    X-ConcurrencyLimit-Remaining | int | The number of concurrent API calls/requests available to be executed in this moment for your API key.

    ### Output data format

    By default we are using JSON output data format for all of our endpoints, you can control format of data by using `output_format` variable in query string parameters.

    #### URL Parameters

    Parameter | Type | Description
    ---------- | ------- | -------
    output_format | string | Output data format *(optional, default value is `json`, possible values are `json`, `xml` or `csv`)*
    csv_include_header | bool | Ignore header line in CSV output? *(optional, default value is `true`, `true` to include CSV header line, `false` otherwise)*
    csv_include_quotes | bool | Encapsulate strings with quotes in CSV output? *(optional, default value is `false`, `true` to encapsulate all strings with `\"`, `false` to leave them unquoted)*
    csv_exclude_col | string | Comma delimited list of column names to ignore in CSV output *(optional, by default all columns are included)*
    csv_set_delimiter | string | Character that will be used as column delimiter in CSV output *(optional, default value is `;`)*
    csv_set_dec_mark | string | Character that will be used as decimal separator in CSV output *(optional, default value is `.`)*
    csv_set_timeformat | string | Format for datetime type in CSV output or `unix` for unix timestamp *(optional, default value is `yyyy-MM-ddTHH:mm:ss.fffffffZ`)*
    csv_set_newline | string | New line type *(optional, default value is `unix`, possible values `win`, `mac`, `unix`)*

    ### Excel / G-Sheets

    There are several ways to use data from our REST API inside the Excel, Google Sheets, or similar calculation sheet application. This section will do as best as possible to keep all information up to date on how you could load the data into these applications. Feel free to contact support if we are missing an option.

    #### CSV download, import:

     1. Open the data in the CSV format from the browser eg. ```https://rest.coinapi.io/v1/exchangerate/USD?apikey=YOUR_API_KEY&invert=true&output_format=csv```
     2. Save the data to the file with the .csv extension.
     3. Use the file saved and import it into the software.
     4. When configuring import, refer to the parameters like delimiter from the [Output data format](#output-data-format)

    The platform-independent way described above is based on CSV but could also be used in other formats like JSON and XML as long as the software support it, but the import procedure needs to be adjusted accordingly.

    #### Microsoft Excel

     * Use [PowerQuery](https://docs.microsoft.com/en-us/power-query/power-query-what-is-power-query) to load the URL directly into the CSV import without saving the file locally.
     * Use the [=WEBSERVICE](https://support.office.com/en-us/article/webservice-function-0546a35a-ecc6-4739-aed7-c0b7ce1562c4) function to load the API response directly into the sheet, but this will not parse the data; additional processing is required.

    #### Google Sheets

     * Use [=IMPORT](https://support.google.com/docs/answer/3093335?hl=en) function to load the REST API endpoint and automatically parse the CSV format data into the cells. eg. ```=IMPORTDATA(\"https://rest.coinapi.io/v1/exchangerate/USD?apikey=YOUR_API_KEY&invert=true&output_format=csv```

    #### OpenOffice Calc

     * Select the menu Insert -> Sheet From File, 2. In the Insert dialog, put the URL eg. ```https://rest.coinapi.io/v1/exchangerate/USD?apikey=YOUR_API_KEY&invert=true&output_format=csv``` in the File Name box at the bottom. Set the drop-down list next to that to Web Page Query and click Open. The Text Import dialog opens where you can change the defaults if needed.
    """

    metadata: Metadata
    r"""<span data-status-page=\\"28923\\"></span>"""
    exchange_rates: ExchangeRates
    r"""<span data-status-page=\\"28924\\"></span>
    Exchange rate is defined as (VWAP-24H) last 24 hour (rolling window over time) Volume Weighted Average Price across multiple data sources listed on our platform. We are selecting and managing the data sources that are used in the calculation based on multiple factors to provide data of highest quality.

    Algorithm is described below:

      1. Exchange rates are produced from quotes, trades, and metadata datasets.
      1. Symbols that are not data_type = \"SPOT\" are excluded from the calculation.
      1. Symbols from the data sources that were marked by us as not legitimate are excluded from the calculation.
      1. Quotes data where the spread is outside the range of ```<0$; 67%>``` are discarded. `spreadPrc = (ask - bid) / ((ask + bid) / 2)`
      1. The midpoint from the quote data is used as a pricing reference and it's weighted by the passive cumulative volume resting on the best prices.
      1. Volume from the trades is used to weight the midpoint prices in the VWAP24 algorithm.
      1. Midpoint data that has not been updated in the last 5 minutes and 1 second is discarded.
      1. The last 24-hour volume for each symbol is updated every 4 hours when approximately 20% of the data in the sliding window changes (also, the list of eligible markets is updated at the same time).
      1. Everywhere in the algorithm below, we are using asset pairs only from exchanges that have the highest legitimacy rank, and the rest of the exchanges are discarded. As we establish the highest-ranking exchanges that have this data for each asset pair, we ensure that the highest quality data is used for each of them. The rank used for asset pairing is carried over to the following steps.
      1. Every 1 second, we update VWAP24 data for every asset pair across all data sources.
      1. For each asset pair, we also discard data that is outside the 3 sigma range if there are at least 3 exchanges for this asset pair.
      1. From the VWAP24 data, we are creating a tree structure where node/vertex = asset and edge = rate.
      1. By traversing the tree structure using the BFS algorithm and our secret sauce, we are able to establish the final exchange rates.
    """
    indexes: Indexes
    r"""Indexes section of the API is in the Alpha release cycle. Use only for testing, evaluaton and feedback."""
    metrics: Metrics
    r"""<span data-status-page=\\"28933\\"></span>
    Metrics are quantitative measurements used to evaluate the performance and activity of cryptocurrency exchanges. These metrics include:

    1. Trading Volume: The total amount of cryptocurrency traded on an exchange within a specific time period, indicating liquidity and activity.
    1. Market Depth: The level of buy and sell orders at different price levels, providing insights into liquidity and potential price impact.
    1. Order Book: A record of outstanding buy and sell orders for a cryptocurrency, reflecting supply and demand dynamics.
    1. Spread: The difference between the highest bid and lowest ask prices, indicating liquidity and trading costs.
    1. Price Charts: Visual representations of cryptocurrency price movements over time, helping identify trends and inform trading decisions.
    1. Market Cap: The total value of a cryptocurrency calculated by its price multiplied by circulating supply, reflecting relative size and value.
    1. Trading Pairs: Combinations of cryptocurrencies available for trading, including volume, price, and spread for each pair.
    1. User Metrics: Data on active users, new registrations, user retention, and engagement, indicating platform popularity and growth.
    1. Trading Fees: Fees charged for executing trades, including fee structure, discounts, and revenue generated by the exchange.
    1. Security Metrics: Measures assessing the security of an exchange, such as past incidents, user fund protection, and security audits.

    These metrics assist traders and investors in evaluating market activity, liquidity, and the reliability of crypto exchanges for informed decision-making.
    """
    order_book: OrderBook
    r"""<span data-status-page=\\"28929\\"></span>
    This section describes calls related to order book data, also known as books or passive level 2 data.

    :::info
    When requesting current data for a specific symbol, output is not encapsulated into JSON array as only one item is returned.
    :::

    :::info
    GET `/v1/orderbooks/current` endpoint is charged one request per 100 data points returned after applying a filter defined by filter_symbol_id parameter. If filter symbols target more than one exchange, error is returned.
    :::

    :::info
    When requesting current order book data limited to a single level, then quotes are actually used. This information is important from the perspective that quotes data could be faster than order book data (behavior is dependent solely one the data source) and they can have the size equal to 0 when the size is unknown. Some data sources publish order books and separately quote data (without the sizes) at a higher frequency. In that case, we will merge the order book feed with quotes feed to make sure that our updates are as fast as possible. The quotes will have the size equal to 0 as the value is unknown and the customer can decide if these higher frequency updates without the sizes are valuable or if not then can discard them or ask for at least 2 order book levels (in case of a REST API call). For the data sources that publish order books only or order books and quotes with the sizes then this will not happen.
    :::
    """
    order_book_l3: OrderBookL3
    r"""<span data-status-page=\\"28929\\"></span>
    This section describes calls related to order book data, also known as books or passive level 3 data.
    """
    quotes: Quotes
    r"""Controller for retrieving quotes data, also known as quotes or passive level 1 data."""
    ohlcv: Ohlcv
    r"""<span data-status-page=\\"28926\\"></span>

    API calls described in this section are related to downloading OHLCV *(Open, High, Low, Close, Volume)* timeseries data.
    Each data point of this timeseries represents several indicators calculated from transactions activity inside a time range (period).

    :::info
    OHLCV data primary purpose is to present an overview of the market in human readable form.
    It's often used to visualize market data on charts, websites, and various kinds of reports.
    :::

    :::tip
    CoinAPI expanded the standard OHLCV timeseries by including time of first and last trade and amount of trades executed inside period.
    :::
    """
    trades: Trades
    r"""Controller for retrieving trade data related to executed transactions."""

    sdk_configuration: CoinAPIConfig

    def __init__(
        self,
        api_key: str | Callable[[], str],
        server_idx: int | None = None,
        server_url: str | None = None,
        url_params: dict[str, str] | None = None,
        client: httpx.Client | None = None,
    ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param api_key: The api_key required for authentication
        :type api_key: Union[str, Callable[[], str]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The httpx.Client HTTP client to use for all operations
        :type client: Optional[httpx.Client]
        """
        if callable(api_key):

            def security() -> components.Security:
                return components.Security(api_key=api_key())
        else:
            security = components.Security(api_key=api_key)  # type: ignore[assignment]

        if server_url is not None and url_params is not None:
            server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = CoinAPIConfig(
            client,
            security,
            server_url,
            server_idx,
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url,
            self.sdk_configuration.client,
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        self.sdk_configuration._hooks = hooks  # noqa: SLF001

        self._init_sdks()

    def _init_sdks(self) -> None:
        self.metadata = Metadata(self.sdk_configuration)
        self.exchange_rates = ExchangeRates(self.sdk_configuration)
        self.indexes = Indexes(self.sdk_configuration)
        self.metrics = Metrics(self.sdk_configuration)
        self.order_book = OrderBook(self.sdk_configuration)
        self.order_book_l3 = OrderBookL3(self.sdk_configuration)
        self.quotes = Quotes(self.sdk_configuration)
        self.ohlcv = Ohlcv(self.sdk_configuration)
        self.trades = Trades(self.sdk_configuration)
