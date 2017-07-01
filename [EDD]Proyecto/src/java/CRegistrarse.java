import java.io.IOException;
import java.io.PrintWriter;
import java.net.MalformedURLException;
import java.net.URL;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
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
public class CRegistrarse extends HttpServlet {

 public static OkHttpClient webClient = new OkHttpClient();
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            String user=request.getParameter("username");
            String pass=request.getParameter("password");
            String pass2=request.getParameter("password2");
            try{
                RequestBody formBody = new FormEncodingBuilder()
                .add("usuario", user)
                .add("contra",pass)
                .add("contra2",pass2)
                .build();
                String r = getString("RegistrarUsuario", formBody);
                response.sendRedirect("Principal.jsp");                
                System.out.println(r + " pos funciona ");
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
