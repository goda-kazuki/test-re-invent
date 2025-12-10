import json
import ldclient
from ldclient import Context
from ldclient.config import Config

# LaunchDarkly SDKキー
LD_SDK_KEY = "sdk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# LaunchDarklyクライアントの初期化
ldclient.set_config(Config(LD_SDK_KEY))


def lambda_handler(event, context):
    # LaunchDarklyクライアントを取得
    ld_client = ldclient.get()

    # コンテキストを作成
    ld_context = Context.create("anonymous")

    # フィーチャーフラグを評価
    flag_key = "hello-lambda-flag"
    flag_value = ld_client.variation(flag_key, ld_context, False)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
                "feature_flag": flag_key,
                "flag_enabled": flag_value,
            }
        ),
    }
