from multiprocessing import Process


def run_inference_job() -> None:
    process = Process(name='Inference', target=run_inference)

    process.daemon = True
    process.start()


def run_training_job() -> None:
    process = Process(name='Training', target=run_train)

    process.daemon = True
    process.start()


def run_inference():
    pass

def run_train(request: dict) -> str:
    pass
