```python
import coinapi

s = coinapi.CoinAPI(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.metadata.get_v1_assets(filter_asset_id='<value>', include_supply=False)

if res.content is not None:
    # handle response
    pass
```