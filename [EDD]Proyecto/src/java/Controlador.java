import java.io.IOException;
import java.io.PrintWriter;
import java.net.MalformedURLException;
import java.net.URL;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
//import javax.ws.rs.core.Request;
//import javax.ws.rs.core.Response;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.util.logging.Level;

/**
 *
 * @author MJoe
 */
public class Controlador extends HttpServlet {

   public static OkHttpClient webClient = new OkHttpClient();
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            String user=request.getParameter("username");
            String pass=request.getParameter("password");
            try{
                 //String param = "paramettro";
                RequestBody formBody = new FormEncodingBuilder()
                .add("usuario", user)
                .add("contra",pass)
                .build();
                String r = getString("IniciarUsuario", formBody);
                response.sendRedirect("Sesion.jsp");
                
                System.out.println(r + " pos funciona iniciar sesion");
                
//                if(user!=null && pass!=null){
//                    if(user.equals("yo") && pass.equals("yo")){
//                        response.sendRedirect("Sesion.jsp");
//                    }else{
//                        out.println("Datos incorrectos, por favor intente de nuevo.");
//                    }
//                }
            }catch(Exception ex){
                out.println("Error we: "+ ex.toString());
            }
        }
    }
    public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(Controlador.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Controlador.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doGet(request, response);
    }
}
