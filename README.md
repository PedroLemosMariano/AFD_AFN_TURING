<h1 align="center">🧩 Simulador de SFD, FN e Máquina de Turing</h1>

<h3 align="center">Projeto desenvolvido na disciplina de Teoria da Computação — UFV - Campus Rio Paranaíba 🎓</h3>

---

## 📘 Sobre o projeto

Este repositório contém a implementação e análise de três dos principais conceitos da **Teoria da Computação**:

- **AFD (Autmatos Finitos Determinístico)**  
- **AFN (Autmatos Finitos não Determinísticos)**  
- **Máquina de Turing**

O objetivo é compreender, simular e visualizar o funcionamento de autômatos e máquinas computacionais formais por meio de código Python, permitindo observar como linguagens formais são processadas e reconhecidas por diferentes modelos computacionais.

---

## 🎯 Objetivos

- Implementar um **Simulador de Autômatos Finitos Determinísticos (AFD)** e **Funções de Transição**;  
- Simular o funcionamento de uma **Máquina de Turing**;  
- Compreender as diferenças de poder computacional entre AFDs, AFNs e Máquinas de Turing;  
- Criar uma **interface interativa (Streamlit)** para visualização e teste de autômatos;  
- Facilitar o estudo e o ensino de Teoria da Computação de forma prática e visual.

---

## ⚙️ Tecnologias utilizadas

<div align="center">

| Categoria | Ferramentas |
|------------|-------------|
| Linguagem | 🐍 **Python** |
| Visualização de autômatos | `graphviz`, `os` |
| Interface gráfica | `Streamlit` |
| Manipulação e simulação | Estruturas e funções definidas em Python |
| Organização de projeto | `UML`, módulos e pacotes |

</div>


---

## 🧠 Metodologia

1. **Modelagem teórica**  
   - Definição formal dos componentes de um AFD e de uma Máquina de Turing;  
   - Elaboração de diagramas UML para representar as classes e suas relações.  

2. **Implementação em Python**  
   - Criação de classes para **estados, transições e alfabetos**;  
   - Simulação passo a passo da execução dos autômatos;  
   - Construção de métodos para verificar aceitação de cadeias.  

3. **Visualização gráfica**  
   - Uso do `graphviz` para gerar o diagrama do autômato;  
   - Interface Streamlit para testar cadeias e observar transições em tempo real.  

4. **Extensão para Máquina de Turing**  
   - Implementação de fitas, cabeçote e função de transição δ(q, a);  
   - Simulação da leitura, escrita e movimentação da fita.  

---

## 💻 Exemplos de uso

- Simular a aceitação de uma cadeia por um AFD:  
  ```python
  from automatos.afd import AFD

  afd = AFD(estados, alfabeto, transicoes, estado_inicial, estados_finais)
  resultado = afd.processar("abba")
  print("Cadeia aceita!" if resultado else "Cadeia rejeitada.")

  streamlit run main.py

##📊 Resultados esperados

Compreensão prática do funcionamento de autômatos finitos e máquinas de Turing;

Visualização clara de transições e estados;

Ferramenta útil para ensino e demonstração em sala de aula;

Base sólida para a expansão do simulador, incluindo autômatos não determinísticos e linguagens regulares.

##👨‍💻 Autor

Pedro Lemos
Estudante de Sistemas de Informação – Universidade Federal de Viçosa (UFV)
📧 pedro.lemosmariano@gmail.com
