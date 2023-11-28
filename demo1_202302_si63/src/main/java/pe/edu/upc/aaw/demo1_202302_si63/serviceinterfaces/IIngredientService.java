package pe.edu.upc.aaw.demo1_202302_si63.serviceinterfaces;

import pe.edu.upc.aaw.demo1_202302_si63.entities.Dessert;
import pe.edu.upc.aaw.demo1_202302_si63.entities.Ingredient;

import java.util.List;

public interface IIngredientService {
    public void insert(Ingredient ingredient);
    public List<Ingredient> list();
    public List<String[]> quantity();

}
