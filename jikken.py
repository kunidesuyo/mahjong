def ts_init():
    return {"t012": 0, "t000": 0, "t00": 0, "t01": 0, "t02": 0}

x = ts_init()
y = ts_init()

x["t012"] = 1
print(x)
print(y)