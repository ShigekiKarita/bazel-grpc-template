load("@rules_proto//proto:defs.bzl", "proto_library")
load("@com_github_grpc_grpc//bazel:cc_grpc_library.bzl", "cc_grpc_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "helloworld_proto",
    srcs = ["helloworld.proto"],
)

cc_proto_library(
    name = "helloworld_cc_proto",
    deps = [":helloworld_proto"],
)

cc_grpc_library(
    name = "helloworld_cc_grpc",
    srcs = [":helloworld_proto"],
    grpc_only = True,
    deps = [":helloworld_cc_proto"],
)

cc_binary(
    name = "cc_client",
    srcs = ["client.cc"],
    deps = [
        "@com_github_grpc_grpc//:grpc++",
        "//:helloworld_cc_grpc",
    ],
)

cc_binary(
    name = "cc_server",
    srcs = ["server.cc"],
    deps = [
        "@com_github_grpc_grpc//:grpc++",
        "@com_github_grpc_grpc//:grpc++_reflection",
        "//:helloworld_cc_grpc",
    ],
)

py_test(
    name = "test",
    size = "small",
    srcs = ["test.py"],
    data = [
        ":cc_client",
        ":cc_server",
    ],
    python_version = "PY3",
    srcs_version = "PY3",
)
