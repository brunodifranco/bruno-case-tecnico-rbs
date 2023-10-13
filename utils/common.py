from pandas.core.series import Series
from plotly.graph_objs._figure import Figure

def adf_test(data: Series, 
             p_valor: float, 
             tipo: str) -> str:
    """   
        Realiza o teste de Dickey-Fuller Aumentado (ADF).

        Parameters
        ----------
        data : pandas.core.series.Series
            Série temporal na qual o teste será aplicado.

        p_valor : float
            p-valor desejado.

         tipo : str
            Significado da coluna na qual o teste será aplicado. 
            ex: Conversões Diretas, Indiretas, etc.  
              
        Returns
        -------
        Resultado do teste: str 
    
    """  

    from statsmodels.tsa.stattools import adfuller
    result = adfuller(data)

    print(f"Teste para {tipo}")
    print(f"Valor de p: {result[1]}")
    

    p_valor = 0.01
    if result[1] <= p_valor:
        return(f"A série é estacionária com significância de {(1- p_valor)*100}%.")
        
    else:
        return(f"A série não é estacionária com significância de {(1- p_valor)*100}%.")
    
def teste_espectro_fourier(data: Series, 
                           tipo: str) -> Figure:
    """   
        Realiza o teste de Análise Espectral, utilizando uma Transformada de Fourier.

        Parameters
        ----------
        data : pandas.core.series.Series
            Série temporal na qual o teste será aplicado.

        tipo : str
            Significado da coluna na qual o teste será aplicado. 
            ex: Conversões Diretas, Indiretas, etc.  
              
        Returns
        -------
        fig : plotly.graph_objs._figure.Figure
            Plot do teste 
    
    """  
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    fs_values = [1, 7, 15, 30] 
    fig = make_subplots(rows=2, cols=2,
                        subplot_titles=[f'Qtd de Dias do Teste = {fs}' for fs in fs_values])
    
    for i, j in enumerate(fs_values):

        fft_result = np.fft.fft(data)
        freqs = np.fft.fftfreq(len(data), 1/j)
        amplitudes = np.abs(fft_result)
        df_fft = pd.DataFrame({'freq': freqs, 'amplitude': amplitudes})
        fig.add_trace(go.Scatter(x=df_fft['freq'].values, y=df_fft['amplitude'].values), row=i // 2 + 1, col=i % 2 + 1)

    fig.update_layout(height=650, width=1000, title_text=f"Espectro de Frequência com Transformada de Fourier para 1, 7, 15 e 30 dias - {tipo}")
   
    return fig
