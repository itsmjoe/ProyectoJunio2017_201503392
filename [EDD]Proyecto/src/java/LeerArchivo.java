
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
import static com.sun.corba.se.spi.presentation.rmi.StubAdapter.request;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.logging.Level;
import javax.servlet.http.HttpSession;

/**
 *
 * @author MJoe
 */
public class LeerArchivo extends HttpServlet {

    public static OkHttpClient webClient = new OkHttpClient();
    public String direccion = "";

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            direccion = request.getParameter("urlarchivo");
            String tarchivo = request.getParameter("tipoarchivo");
            System.out.println(tarchivo + " ajaja pos funciona iniciar sesion");
            try {
                switch (tarchivo) {
                    case "1":
                        LeerJuego();
                        break;
                    case "2":
                        LeerJuegoActual();
                        break;
                    case "3":
                        LeerNaves();
                        break;
                    case "4":
                        LeerUsuarios();
                        break;
                }

            } catch (Exception ex) {
                out.println("Error we: " + ex.toString());
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
    private void LeerUsuarios() throws FileNotFoundException, IOException {
        //To change body of generated methods, choose Tools | Templates.
        String thisLine;
        FileInputStream fis = new FileInputStream(direccion);
        DataInputStream myInput = new DataInputStream(fis);
        int i = 0;
        while ((thisLine = myInput.readLine()) != null) {
            String strar[] = thisLine.split(",");
            
                String user = strar[0];
                String pass = strar[1];
                String estado = strar[2];
            if (user == null ? ("Usuario") == null : user.equals("Usuario")) {
            } else {
                RequestBody formBody = new FormEncodingBuilder()
                        .add("usuario", user)
                        .add("contra", pass)
                        .add("estado", estado)
                        .build();
                String r = getString("IngresarUsuario", formBody);
                System.out.println(user+" insertado");
            }
        }
    }

    private void LeerJuego() throws FileNotFoundException, IOException {
         //To change body of generated methods, choose Tools | Templates.
        String thisLine;
        FileInputStream fis = new FileInputStream(direccion);
        DataInputStream myInput = new DataInputStream(fis);
        int i = 0;
        while ((thisLine = myInput.readLine()) != null) {
            String strar[] = thisLine.split(",");            
                String user1 = strar[0];
                String user2= strar[1];
                String tirosl = strar[2];
                String tirosa = strar[3];
                String tirosf = strar[4];
                String estadojuego = strar[5];
                String danio = strar[6];
            if (user1 == null ? ("Usuario Base") == null : user1.equals("Usuario Base")) {
            } else {
                RequestBody formBody = new FormEncodingBuilder()
                        .add("usuario", user1)
                        .add("oponente", user2)
                        .add("lanzados", tirosl)
                        .add("acertados", tirosa)
                        .add("fallados", tirosf)
                        .add("estadojuego", estadojuego)
                        .add("danio", danio)
                        .build();
                String r = getString("IngresarJuego", formBody);
                System.out.println(user1+" "+user2+" insertado");
            }
        }
    }

    private void LeerJuegoActual() throws FileNotFoundException, IOException {
        //To change body of generated methods, choose Tools | Templates.
        String thisLine;
        FileInputStream fis = new FileInputStream(direccion);
        DataInputStream myInput = new DataInputStream(fis);
        int i = 0;
        while ((thisLine = myInput.readLine()) != null) {
            String strar[] = thisLine.split(",");            
                String user1 = strar[0];
                String user2= strar[1];
                String tamX = strar[2];
                String tamY = strar[3];
                String variante = strar[4];
                String tiempo = strar[5];
                String disparo = strar[6];
                String nrafagas = strar[7];
                //HttpSession VariableSesion= request.getSession(true);;
              //  VariableSesion.setAttribute("Variante",variante);
               // VariableSesion.setAttribute("Tiempo",tiempo);
               // VariableSesion.setAttribute("Disparo",disparo);
               // VariableSesion.setAttribute("Nrafagas",nrafagas);
               // System.out.println((String)VariableSesion.getAttribute("Disparo"));
               System.out.println(user1+ " "+user2);
            if (user1 == null ? ("Usuario1") == null : user1.equals("Usuario1")) {
            } else {
                RequestBody formBody = new FormEncodingBuilder()
                        .add("usuario", user1)
                        .add("oponente", user2)
                        .add("tamx", tamX)
                        .add("tamy", tamY)
                        .add("variante", variante)
                        .add("tiempo", tiempo)
                        .add("disparo", disparo)
                        .add("nrafagas",nrafagas)
                        .build();
                String r = getString("IngresarJuegoActual", formBody);
                System.out.println("Juego actual  "+ r);
            }
        }        
    }

    private void LeerNaves() throws FileNotFoundException, IOException {
        //To change body of generated methods, choose Tools | Templates.
        String thisLine;
        FileInputStream fis = new FileInputStream(direccion);
        DataInputStream myInput = new DataInputStream(fis);
        int i = 0;
        while ((thisLine = myInput.readLine()) != null) {
            String strar[] = thisLine.split(",");            
                String user1 = strar[0];
                String col= strar[1];
                String fila = strar[2];
                String nivel = strar[3];
                String modo = "";
                String dir ="";
                if (nivel.equals("1") || nivel.equals("2")){
                    modo = strar[4];
                    dir = "0";
                }else{
                    modo = strar[4];
                   dir = strar[5];
                }
            
            if (user1 == null ? ("jugador1") == null : user1.equals("jugador1")) {
            } else {                
                RequestBody formBody = new FormEncodingBuilder()
                        .add("usuario", user1)
                        .add("col", col)
                        .add("fila", fila)
                        .add("nivel", nivel)
                        .add("modo", modo)
                        .add("dir", dir)
                        .build();
                String r = getString("IngresarNaves", formBody);
                System.out.println(user1+" "+nivel+" nave ingresada.");
            }
        }
    }
}
