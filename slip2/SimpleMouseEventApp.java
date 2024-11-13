// cd slip2
// javac SimpleMouseEventApp.java
// java SimpleMouseEventApp


import javax.swing.*;
import java.awt.event.*;

public class SimpleMouseEventApp extends JFrame {
    private JTextField textField;

    public SimpleMouseEventApp() {
        
        setTitle("Mouse Event Example");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);

       
        textField = new JTextField();
        textField.setBounds(50, 200, 300, 30);
        add(textField);

  
        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                int x = e.getX();
                int y = e.getY();
                textField.setText("Clicked at: (" + x + ", " + y + ")");
            }
        });

        addMouseMotionListener(new MouseAdapter() {
            @Override
            public void mouseMoved(MouseEvent e) {
           
                System.out.println("Mouse moved to: (" + e.getX() + ", " + e.getY() + ")");
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            SimpleMouseEventApp app = new SimpleMouseEventApp();
            app.setVisible(true);
        });
    }
}
