import dotenv
import pytest
from enums import Market

from csmarketapi import CSMarketAPI


@pytest.fixture(scope="module")
def env():
    env = dotenv.dotenv_values(".env")
    yield env


@pytest.mark.asyncio
async def test_get_listings_latest_aggregated(env):

    async with CSMarketAPI(env["API_KEY"]) as client:

        assert (
            await client.get_listings_latest_aggregated(
                market_hash_name=env["MARKET_HASH_NAME"], markets=list(Market)
            )
        ).listings is not None


@pytest.mark.asyncio
async def test_get_listings_history_aggregated(env):
    async with CSMarketAPI(env["API_KEY"]) as client:

        assert (
            await client.get_listings_history_aggregated(
                market_hash_name=env["MARKET_HASH_NAME"], markets=list(Market)
            )
        ).items is not None


@pytest.mark.asyncio
async def test_get_sales_latest_aggregated(env):
    async with CSMarketAPI(api_key=env["API_KEY"]) as client:

        assert (
            await client.get_sales_latest_aggregated(
                market_hash_name=env["MARKET_HASH_NAME"], markets=list(Market)
            )
        ).sales is not None


@pytest.mark.asyncio
async def test_get_sales_history_aggregated(env):
    async with CSMarketAPI(api_key=env["API_KEY"]) as client:

        assert (
            await client.get_sales_history_aggregated(
                market_hash_name=env["MARKET_HASH_NAME"], markets=list(Market)
            )
        ).items is not None


@pytest.mark.asyncio
async def test_get_items(env):
    async with CSMarketAPI(api_key=env["API_KEY"]) as client:

        assert (await client.get_items()).items is not None


@pytest.mark.asyncio
async def test_get_currency_rates(env):
    async with CSMarketAPI(api_key=env["API_KEY"]) as client:

        assert (await client.get_currency_rates()).items is not None


@pytest.mark.asyncio
async def test_get_player_counts_latest(env):
    async with CSMarketAPI(api_key=env["API_KEY"]) as client:

        assert (await client.get_player_counts_latest()).count is not None


@pytest.mark.asyncio
async def test_get_player_counts_history(env):
    async with CSMarketAPI(api_key=env["API_KEY"]) as client:

        assert (await client.get_player_counts_history()).items is not None


@pytest.mark.asyncio
async def test_get_steam_profile(env):
    async with CSMarketAPI(api_key=env["API_KEY"]) as client:

        assert (
            await client.get_steam_profile(steam_id=env["STEAM_ID"])
        ).data is not None


@pytest.mark.asyncio
async def test_get_steam_inventory(env):
    async with CSMarketAPI(api_key=env["API_KEY"]) as client:

        assert (
            await client.get_steam_inventory(steam_id=env["STEAM_ID"])
        ).steamid is not None


@pytest.mark.asyncio
async def test_get_steam_friendslist(env):
    async with CSMarketAPI(api_key=env["API_KEY"]) as client:

        assert (
            await client.get_steam_friendslist(steam_id=env["STEAM_ID"])
        ).data is not None


@pytest.mark.asyncio
async def test_get_float_info(env):
    async with CSMarketAPI(api_key=env["API_KEY"]) as client:

        await client.get_float_info(inspect_link=env["INSPECT_LINK"])
