package practice.junit;

import static org.junit.Assert.*;
import org.junit.*;
import org.junit.jupiter.api.DisplayName;

public class CalculatorTest {
   
   @Test
   @DisplayName("calculator test")
   public void testDivide() {
      
      //NaN
      assertTrue(Calculator.divide(0, 0) == 0);
      
      //Infinity
      assertTrue(Calculator.divide(100, 0) == 0);

      assertTrue(Calculator.divide(0, 100) == 0);
      assertTrue(Calculator.divide(1, -100) == -0.01);
      assertTrue(Calculator.divide(-100, 100) == -1);
      assertTrue(Calculator.divide(-100, -100) == 1);
   }

   @Test
   public void testFahrenheitToCelsius() {
      assertTrue(Calculator.FahrenheitToCelsius(0) == -17.77777777777778);
      assertTrue(Calculator.FahrenheitToCelsius(100) == 37.77777777777778);
      assertTrue(Calculator.FahrenheitToCelsius(-100) == -73.33333333333333);
   }
   
   @Test
   public void testCelsiusToFahrenheit() {
      assertTrue(Calculator.CelsiusToFahrenheit(0) == 32);
      assertTrue(Calculator.CelsiusToFahrenheit(100) == 212);
      assertTrue(Calculator.CelsiusToFahrenheit(-100) == -148);
   }
}