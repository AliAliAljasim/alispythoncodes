async def main():
    ably = AblyRealtime('xVLyHw.vW1ihQ:UoEJTcPU9I9bw0Gj6bt_YHHUn37T1aA8b-1mh1PV8-w')
    await ably.connection.once_async('connected')
    print("Connected to Ably")
