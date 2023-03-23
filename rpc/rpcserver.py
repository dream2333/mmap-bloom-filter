import zerorpc

class HelloRPC(object):
    count = 0
    def hello(self, name):
        '''
        测试rpc
        '''
        self.count+=1
        return self.count

s = zerorpc.Server(HelloRPC(),pool_size=100)
s.bind("tcp://0.0.0.0:4242")
s.run()