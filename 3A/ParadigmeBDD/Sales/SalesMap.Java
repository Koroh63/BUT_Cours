
package demos;

import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.IntWritable;
import java.util.StringTokenizer;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;


// Notre classe MAP.
public class SalesMap extends Mapper<Object, Text, Text, Double>
{
	

	// La fonction MAP elle-même.
	protected void map(Object key, Text value, Context context) throws IOException, InterruptedException
	{  
        
		String[] tab=value.toString(), ",";
        switch(context.getConfiguration().get("operation")){
            case "profitPerRegion":
                if(!region.equals("Region")):
                    context.write(tab[0],Double.parseDouble(tab[13]));
                    context.write("Total : ",Double.parseDouble(tab[13]));
                break;
            case "profitPerCountry":
                if(!region.equals("Region")):
                    context.write(tab[1],Double.parseDouble(tab[13]));
                    context.write("Total : ",Double.parseDouble(tab[13]));
                break;
            case "profitPerItem":
                if(!region.equals("Region")):
                    context.write(tab[2],Double.parseDouble(tab[13]));
                    context.write("Total : ",Double.parseDouble(tab[13]));
                break;
            case "profitPerItemSeparate":
                if(!region.equals("Region")):
                    context.write(new String(tab[2]+" - "+tab[3]),Double.parseDouble(tab[13]));
                    context.write("Total : ",Double.parseDouble(tab[13]));
                break;
            default:
                if(!region.equals("Region")):
                    context.write("Total : ",Double.parseDouble(tab[13]));
                break;
        }
            
                
    }
}
