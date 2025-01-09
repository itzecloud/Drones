## Introducción
¿Cómo se mide la distancia entre las estrellas? Los astrónomos han descubierto ingeniosos métodos para hacerlo. Los dos principales son el paralaje y el uso de candelas estándar, es decir, eventos u objetos que comparten características comunes que permiten conocer su brillo. Un tipo de velas son las conocidas como cefeidas, que son estrellas que brillan de forma periódica en apenas días o menos como se muestra a continuación. A diferencia del resto de estrellas que cambian de brillo sólo debido a fluctuaciones «aleatorias», o al envejecimiento estelar que tarda millones de años. En este caso las buscaremos utilizando los datos de Kepler. 

## Metodología.
Para encontrar tales cefeidas tenemos que realizar una regresión senoidal a nuestros datos. En general, las cefeidas deben parecerse a una curva seno/coseno. Para encontrar tales estrellas, se creó un script python usando la implementación de la Transformada Rápida de Fourier de Sci-py. Finalmente creé un informe Power BI que utiliza Python Visuals. 

## Results Overwiew.
Los resultados del nuevo método se muestran a continuación. Nota: Tienes que instalar Python, Power BI, Pandas, NUmpy y Matplotlib para que funcione. Una vez instalado pega los ficheros appended_fluxes.csv y new_method_sample.csv en tu carpeta de documentos así como el fichero StarVisualizar.pbix. Abra StarVisualizar.pbix una vez instalado python. Puede encontrar una explicación más completa de cómo hacerlo aquí: https://monics-hub.blogspot.com/2025/01/como-descargar-starvisualizerpbix.html

Puedes ver una explicación de cómo se creo el proyecto en inglés aquí: https://github.com/itzecloud/New-Method-for-Cepheid-Search/blob/main/Senoidal%20Regression%20Algorithm.pdf

Puedes ver la versión web del proyecto aquí: https://app.powerbi.com/view?r=eyJrIjoiNzVhZWU4MTgtMDJhNC00NjA2LWI5OGYtNzkwYjJjMWE0M2UwIiwidCI6ImE4MGU0MjRhLTUzYzMtNGJlYS04NzdhLTc1YmZkMDZlZjIwMyJ9

![foto1](https://github.com/user-attachments/assets/972a152c-cea9-48dd-98c5-bd2bc0ef53ba)
![foto2](https://github.com/user-attachments/assets/0ce9787f-fedf-4c8a-8f3f-29e1cf537769)
![foto3](https://github.com/user-attachments/assets/9a961495-d4a6-455a-86be-e540fa02230d)
