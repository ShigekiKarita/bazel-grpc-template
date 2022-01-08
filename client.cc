/*
 *
 * Copyright 2015 gRPC authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

#include <iostream>
#include <memory>
#include <string>

#include <grpcpp/grpcpp.h>

#include "helloworld.grpc.pb.h"

int main(int argc, char** argv) {
  // We indicate that the channel isn't authenticated (use of
  // InsecureChannelCredentials()).
  std::unique_ptr<helloworld::Greeter::Stub> stub = helloworld::Greeter::NewStub(
      grpc::CreateChannel("localhost:50051", grpc::InsecureChannelCredentials()));
  std::string user("world");

  // Data we are sending to the server.
  helloworld::HelloRequest request;
  request.set_name(user);

  // Container for the data we expect from the server.
  helloworld::HelloReply reply;

  // Context for the client. It could be used to convey extra information to
  // the server and/or tweak certain RPC behaviors.
  grpc::ClientContext context;
  if (grpc::Status status = stub->SayHello(&context, request, &reply); status.ok()) {
    std::cout << "Greeter received: " << reply.message() << std::endl;
  } else {
    std::cout << status.error_code() << ": " << status.error_message()
              << std::endl;
    return status.error_code();
  }

}
