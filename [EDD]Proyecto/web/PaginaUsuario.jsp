<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <title>Pagina del usuario</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <link rel="stylesheet" href="css/style.css">
    </head>
    <body>
        <form action="PaginaUsuario.jsp" method="post">
           <div class="wrap">
		<div class="avatar">
                <img src="logo.png">
		</div>
		<input type="text" name="username" placeholder="username" required/>
		<div class="bar">
			<i></i>
		</div>
		<input type="password" name="password" placeholder="password" required/>
		<a href="" class="forgot_link">forgot?</a>
                <input type="submit" value="Sign in" /> 
                
                
            </div>
        </form>
    </body>
</html>