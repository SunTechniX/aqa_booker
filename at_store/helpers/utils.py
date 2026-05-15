def load_data(mutable_data: dict,
              tokens: str | list[str] | tuple[str],
              instance: str | list[str] | tuple[str]) -> None:
    if isinstance(tokens, str):
        mutable_data["csrftoken"] = tokens
        mutable_data["csrfinstance"] = instance
    else:
        mutable_data["csrftoken"] = tokens[0]
        mutable_data["csrfinstance"] = instance[0]
