# import zerorpc
# from tools import caculate_time
# from concurrent.futures.thread import ThreadPoolExecutor
# from concurrent.futures.process import ProcessPoolExecutor
# @caculate_time
# def run_rpc_client():
#     c = zerorpc.Client()
#     c.connect("tcp://127.0.0.1:4242")
#     def rpc():
#         r = c.hello("hello")
#         print(r)

#     with ThreadPoolExecutor(max_workers=5) as pool:
#         for i in range(10):
#             pool.submit(rpc)


#     # with ProcessPoolExecutor(max_workers=4) as pool:
#     #     for i in range(5):
#     #         pool.submit(run)

# run_rpc_client()