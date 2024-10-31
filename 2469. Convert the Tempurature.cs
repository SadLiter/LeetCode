public class Solution {
    public double[] ConvertTemperature(double celsius) {
        double[] ans = { celsius + 273.15, celsius * 9/5 + 32 };
        return (ans);
    }
}