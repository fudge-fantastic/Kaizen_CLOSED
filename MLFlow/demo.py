import os
import mlflow
import time
import argparse
import sys

def eval(inp1, inp2):
    output_metric = inp1**2 + inp2**2
    return output_metric

def main(param1, param2):
    mlflow.set_experiment("Demo_Experiment")
    # We can specify our own run-name
    # with mlflow.start_run(run_name = "Experiment_1"):
    with mlflow.start_run():
        mlflow.set_tag("version", "1.0.0")
        # These below are in the form of Key-Value pair
        mlflow.log_param("param1", param1)
        mlflow.log_param("param2", param2)
        metric = eval(inp1=param1, inp2=param2)
        mlflow.log_metric("Eval_metric", metric)
        os.makedirs("Demo", exist_ok=True)
        with open("Demo/example.txt", 'wt') as f:
            f.write(f"Artifact created at: {time.asctime()}")
        mlflow.log_artifact("Demo")

        
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--param1", dest="p1", type=int, default=5)
    args.add_argument("--param2", dest="p2", type=int, default=10)
    parsed_args = args.parse_args(sys.argv[1:])
    # To access any parameters, simply put:
    main(parsed_args.p1, parsed_args.p2)
