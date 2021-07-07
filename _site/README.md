# Blog The Dojo MX

En este blog hablamos de:

- Desarrollo de software en general
- Lenguajes de programación
- Documentación, pruebas y buenas prácticas de mantenimiento
- Desarrollo de productos digitales
- Análisis de datos
- Inteligencia artificial
- Aprendizaje en general (enfocado en programación)

## Acerca de este blog

Intentamos mejorar el ecosistema de desarrollo en español.

### ¿A quiénes está dirigido este blog?

Personas interesadas en el desarrollo de software en general, pero sobre todo que quieran desarrollar sus habilidades en los temas mencionados arriba.

### Publicaciones

Este es un blog open source. Si quieres participar con un artículo manda un PR. Serán considerados los artículos con las siguientes características:

- Tienen información útil, que sea interesante para el público de este blog.
- Información práctica, que se pueda aplicar.
- Información actual pero que aguante el paso del tiempo.
- Tutoriales bien escritos bienvenidos.


### Para publicar
gem install bundler:2.1.2
bundle install
jekyll serve

export JEKYLL_ENV=production

jekyll build -d docs



Necesitamos actualizar los flights o en su defecto ligarlos a un trip para posteriormente actualizar el trip y así poder sincronizar la infromacion que tenemos en la app con Astro para lo cual buscamos alguna de las siguientes soluciones:

1. Poder actualizar los pasajeros de un ferrie, en este caso lo que se probó fue actualizar un ferry mandandole la misma informacion(sin modificar) que recibimos del endpoint /Extensions/Presentation/operations.svc/flight/{flightIDStr}
pero el resultado fue el siguiente:{
"ActivityID":"55eb564e-daa1-4173-bd52-335157df3ce3",
"Detail":"   at DJT.Database.JSCCommand.ExecuteNonQuery() in D:\\Build\\ASTRO\\agent\\_work\\3\\s\\test-branch\\Source\\Framework\\DJT.Database\\JSCCommand.cs:line 297\r\n   at DJT.Database.DBUtil.ExecuteNonQuery(JSCCommand cmd, IConnectionInfo connectionInfo, IsolationLevel isolationLevel) in D:\\Build\\ASTRO\\agent\\_work\\3\\s\\test-branch\\Source\\Framework\\DJT.Database\\DBUtil.cs:line 801",
"ErrorMessage":"Error occurred executing '[ASTRO_STAGE].dbo.sp_AddFlightsExt'\r\nAdditional Information: Cannot insert the value NULL into column 'MinRequiredFuel', table 'ASTRO_STAGE.dbo.tm_FlightsExt'; column does not allow nulls. INSERT fails.\r\nThe statement has been terminated."
}

2. Lograr crear un trip a partir de un flight existente (Flight que no está ligado ningún trip).



