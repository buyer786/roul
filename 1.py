import websockets, asyncio

for x in range(150):
        x=1
        async def Forward():
                url = 'ws://https://evolive.gpms365.net/public/roulette/player/game/SpeedAutoRo00001/socket?messageFormat=json&instance=jwycmr-og6rgd77nou5y5jc-q5be7b6m6uydstfi&tableConfig=q5be7b6m6uydstfi&EVOSESSIONID=og6rgd77nou5y5jcrl5t6s3arrohtr2d08996ec04b0d0702409d99c99bad4bbe4e23d1c841160317&client_version=6.20231003.72237.32124-60ed290cb7'
                async with websockets.connect(url) as websocket:
                        await websocket.send({"id":"1696434625535-824","type":"roulette.tableState","args":{"state":"GAME_RESOLVED","gameId":"178af2479fd8a2787394d15b","gameNumber":"15:49:59","result":["5"],"idleRounds":2,"betState":{"spinNowAllowed":false,"balanceId":"combined","lastGameChips":{}}},"time":1696434625535})
        def xmit_Loop():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(Forward({"id":"1696434625535-824","type":"roulette.tableState","args":{"state":"GAME_RESOLVED","gameId":"178af2479fd8a2787394d15b","gameNumber":"15:49:59","result":["5"],"idleRounds":2,"betState":{"spinNowAllowed":false,"balanceId":"combined","lastGameChips":{}}},"time":1696434625535}))

        x=x+1

