package pe.edu.upc.aaw.demo1_202302_si63.entities;

import javax.persistence.*;

@Entity
@Table(name = "Ingredient")
public class Ingredient {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int idIngredient;
    @Column(name = "nameIngredient", nullable = false, length = 30)
    private String nameIngredient;
    @Column(name = "amountIngredient", nullable = false)
    private double amountIngredient;
    @Column(name = "typeIngredient", nullable = false, length = 30)
    private String typeIngredient;
    @ManyToOne
    @JoinColumn(name = "idDessert")
    private Dessert dessert;

    public Ingredient() {
    }

    public Ingredient(int idIngredient, String nameIngredient, double amountIngredient, String typeIngredient, Dessert dessert) {
        this.idIngredient = idIngredient;
        this.nameIngredient = nameIngredient;
        this.amountIngredient = amountIngredient;
        this.typeIngredient = typeIngredient;
        this.dessert = dessert;
    }

    public int getIdIngredient() {
        return idIngredient;
    }

    public void setIdIngredient(int idIngredient) {
        this.idIngredient = idIngredient;
    }

    public String getNameIngredient() {
        return nameIngredient;
    }

    public void setNameIngredient(String nameIngredient) {
        this.nameIngredient = nameIngredient;
    }

    public double getAmountIngredient() {
        return amountIngredient;
    }

    public void setAmountIngredient(double amountIngredient) {
        this.amountIngredient = amountIngredient;
    }

    public String getTypeIngredient() {
        return typeIngredient;
    }

    public void setTypeIngredient(String typeIngredient) {
        this.typeIngredient = typeIngredient;
    }

    public Dessert getDessert() {
        return dessert;
    }

    public void setDessert(Dessert dessert) {
        this.dessert = dessert;
    }
}
