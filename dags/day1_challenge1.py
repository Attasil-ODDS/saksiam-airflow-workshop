from airflow import DAG
from airflow.utils import timezone 
from airflow.operators.dummy import DummyOperator

default_args = {
  "owner": "Attasil Chitwirote",
  "start_date": timezone.datetime(2021, 9, 27)
}

with DAG(
  "day1_challenge1",
  schedule_interval="*/10 * * * *",
  default_args=default_args,
  catchup=False,
  tags=["saksiam"]
) as dag:

  node1 = DummyOperator(task_id="1")
  node2 = DummyOperator(task_id="2")
  node3 = DummyOperator(task_id="3")
  node4 = DummyOperator(task_id="4")
  node5 = DummyOperator(task_id="5")
  node6 = DummyOperator(task_id="6")
  node7 = DummyOperator(task_id="7")
  node8 = DummyOperator(task_id="8")
  node9 = DummyOperator(task_id="9")

  # node1 >> node2 >> node3 >> node4 >> node9
  # node2 >> node6 >> node8 >> node9
  # node1 >> node5 >> [node6, node7] >> node8 >> node9

  node1 >> [node2, node5] >> node6 >> node8 >> node9
  node2 >> node3 >> node4 >> node9
  node5 >> node7 >> node8

