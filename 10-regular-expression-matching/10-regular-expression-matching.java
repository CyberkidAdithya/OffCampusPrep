import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;

class Solution {
    public boolean isMatch(String s, String p) throws PatternSyntaxException {
        return Pattern.compile(p).matcher(s).matches();
    }
}