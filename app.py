import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import sorting_algorithms as sorting


def main():
    t_1 = "Comparing sorting algorithms performances"
    st.title(t_1)

    input_sizes = (10, 100, 1000)
    n_of_runs = 10

    # Performance calculation
    with st.spinner("Calculating..."):
        results = sorting.performance_test(input_sizes, n_of_runs)

    st.subheader("Table of results (avg time in seconds)")
    st.write("Sizes tested:", input_sizes)
    st.write("Average calculated on:", n_of_runs, "runs")

    # Create a df to show the results
    df = pd.DataFrame(results, index=input_sizes)
    df.index.name = "Input size"
    st.dataframe(df)

    # Plot the results
    fig, ax = plt.subplots(figsize=(8, 5))

    for algo_name, times in results.items():
        ax.plot(input_sizes, times, marker="o", label=algo_name)

    ax.set_xlabel("Input size")
    ax.set_ylabel("Avg time (s)")
    ax.set_title(t_1)
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)


if __name__ == "__main__":
    main()
