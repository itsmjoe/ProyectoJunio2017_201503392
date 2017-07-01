<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>Sesion iniciada</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <link rel="stylesheet" href="css/style.css">
    </head>
    <body>
        <form action="LeerArchivo" method="post">
            <h1>Leer archivo<h1/> 
            <input type="text" style="width:400px" name="urlarchivo" placeholder="URL archivo" required/>            
            
            <input type="submit" value="Leer archivo" /> 
            <div></<div>
            <select name="tipoarchivo" size="1">
            <option value="1">Archivo de Juegos</option>
            <option value="2">Archivo de Juego Actual</option>
            <option value="3">Archivo de Naves</option>
            <option value="4">Archivo de Usuarios</option>
        </form>
    </body>
</html>
