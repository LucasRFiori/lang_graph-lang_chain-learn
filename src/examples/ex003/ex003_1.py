import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph
from rich import print


def reducer(a: list[str], b: list[str]) -> list[str]:
    reducer_result = a + b
    print("> reducer em execução", f"{reducer_result=}")
    return reducer_result


class State(TypedDict):
    nodes_path: Annotated[list[str], operator.add]


def node_a(state: State) -> State:
    final_state: State = {"nodes_path": ["A"]}
    print("> node_a em execução", f"{state=}", f"{final_state=}")
    return final_state


def node_b(state: State) -> State:
    final_state: State = {"nodes_path": ["B"]}
    print("> node_b em execução", f"{state=}", f"{final_state=}")
    return final_state


print("Criando o StateGraph")
builder = StateGraph(State)

print("Adicionando os nodes")
builder.add_node("A", node_a)
builder.add_node("B", node_b)

print("Conectando as edges")
builder.add_edge(START, "A")
builder.add_edge("A", "B")
builder.add_edge("B", END)

print("Compilando o grafo...")
graph = builder.compile()

print()
print("Executando o grafo com `invoke`")
response = graph.invoke({"nodes_path": []})
print()

print("Aqui está o resultado final...")
print(f"{response=}")
print()


response = {"nodes_path": ["A", "B"]}
