package pe.edu.upc.aaw.demo1_202302_si63.dtos;

import pe.edu.upc.aaw.demo1_202302_si63.entities.Dessert;

public class IngredientDTO {
    private int idIngredient;
    private String nameIngredient;
    private double amountIngredient;
    private String typeIngredient;

    private Dessert dessert;

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
