package pe.edu.upc.aaw.demo1_202302_si63.entities;



import javax.persistence.*;
import java.time.LocalDate;
@Entity
@Table(name ="Dessert" )
public class Dessert {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int idDessert;
    @Column(name = "nameDessert",nullable = false,length = 40)
    private String nameDessert;
    @Column(name = "dueDateDessert",nullable = false)
    private LocalDate dueDateDessert;
    @Column(name = "typeDessert",nullable = false,length = 20)
    private String typeDessert;
    @Column(name = "caloryDessert",nullable = false)
    private int caloryDessert;

    public Dessert() {
    }

    public Dessert(int idDessert, String nameDessert, LocalDate dueDateDessert, String typeDessert, int caloryDessert) {
        this.idDessert = idDessert;
        this.nameDessert = nameDessert;
        this.dueDateDessert = dueDateDessert;
        this.typeDessert = typeDessert;
        this.caloryDessert = caloryDessert;
    }

    public int getIdDessert() {
        return idDessert;
    }

    public void setIdDessert(int idDessert) {
        this.idDessert = idDessert;
    }

    public String getNameDessert() {
        return nameDessert;
    }

    public void setNameDessert(String nameDessert) {
        this.nameDessert = nameDessert;
    }

    public LocalDate getDueDateDessert() {
        return dueDateDessert;
    }

    public void setDueDateDessert(LocalDate dueDateDessert) {
        this.dueDateDessert = dueDateDessert;
    }

    public String getTypeDessert() {
        return typeDessert;
    }

    public void setTypeDessert(String typeDessert) {
        this.typeDessert = typeDessert;
    }

    public int getCaloryDessert() {
        return caloryDessert;
    }

    public void setCaloryDessert(int caloryDessert) {
        this.caloryDessert = caloryDessert;
    }
}
