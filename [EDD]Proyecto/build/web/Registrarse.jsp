<%-- 
    Document   : Registrarse
    Created on : Jun 21, 2017, 8:37:55 PM
    Author     : MJoe
--%>
<html>
    <head>
        <title>Registrarse</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <link rel="stylesheet" href="css/style.css">
    </head>
    <body>
        <form action="CRegistrarse" method="post">
           <div class="wrap">
		<div class="avatar">
                <img src="logo.png">
		</div>
		<input type="text" name="username" placeholder="username" required/>
		<div class="bar">
			<i></i>
		</div>
		<input type="password" name="password" placeholder="password" required/>
                <div class="bar">
			<i></i>
		</div>               
		<input type="password" name="password2" placeholder="password" required/>
		<a href="Principal.jsp" class="forgot_link">Iniciar sesion</a>
                <input type="submit" value="Registrarse" /> 
            </div>
        </form>
    </body>
</html>
