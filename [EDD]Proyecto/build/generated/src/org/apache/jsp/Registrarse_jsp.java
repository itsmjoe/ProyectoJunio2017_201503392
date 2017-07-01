package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class Registrarse_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("<html>\n");
      out.write("    <head>\n");
      out.write("        <title>Registrarse</title>\n");
      out.write("        <meta charset=\"UTF-8\">\n");
      out.write("        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n");
      out.write("         <link rel=\"stylesheet\" href=\"css/style.css\">\n");
      out.write("    </head>\n");
      out.write("    <body>\n");
      out.write("        <form action=\"Controlador\" method=\"post\">\n");
      out.write("           <div class=\"wrap\">\n");
      out.write("\t\t<div class=\"avatar\">\n");
      out.write("                <img src=\"logo.png\">\n");
      out.write("\t\t</div>\n");
      out.write("\t\t<input type=\"text\" name=\"username\" placeholder=\"username\" required/>\n");
      out.write("\t\t<div class=\"bar\">\n");
      out.write("\t\t\t<i></i>\n");
      out.write("\t\t</div>\n");
      out.write("\t\t<input type=\"password\" name=\"password\" placeholder=\"password\" required/>\n");
      out.write("\t\t<a href=\"Registrarse.jsp\" class=\"forgot_link\">Registrarse</a>\n");
      out.write("                <input type=\"submit\" value=\"Sign in\" /> \n");
      out.write("            </div>\n");
      out.write("        </form>\n");
      out.write("    </body>\n");
      out.write("</html>\n");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
