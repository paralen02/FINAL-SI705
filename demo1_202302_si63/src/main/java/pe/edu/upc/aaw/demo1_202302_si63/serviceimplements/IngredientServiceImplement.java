package pe.edu.upc.aaw.demo1_202302_si63.serviceimplements;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pe.edu.upc.aaw.demo1_202302_si63.entities.Ingredient;
import pe.edu.upc.aaw.demo1_202302_si63.repositories.IIngredientRepository;
import pe.edu.upc.aaw.demo1_202302_si63.serviceinterfaces.IIngredientService;

import java.util.List;

@Service
public class IngredientServiceImplement implements IIngredientService {
    @Autowired
    private IIngredientRepository iR;

    @Override
    public void insert(Ingredient ingredient) {
        iR.save(ingredient);
    }

    @Override
    public List<Ingredient> list() {
        return iR.findAll();
    }

    @Override
    public List<String[]> quantity() {
        return iR.quantity();
    }

}
