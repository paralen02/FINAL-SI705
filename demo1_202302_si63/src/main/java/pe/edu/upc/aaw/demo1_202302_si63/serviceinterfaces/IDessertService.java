package pe.edu.upc.aaw.demo1_202302_si63.serviceinterfaces;

import pe.edu.upc.aaw.demo1_202302_si63.entities.Dessert;

import java.time.LocalDate;
import java.util.List;

public interface IDessertService {
    public void insert(Dessert dessert);
    public List<Dessert> list();
    public void delete(int idDessert);
    public Dessert listarId(int idDessert);
    List<Dessert> findByDueDateDessert(LocalDate dueDateDessert);
}
