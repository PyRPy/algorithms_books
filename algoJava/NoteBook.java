package notebook;

import java.util.ArrayList;

public class NoteBook {
	private ArrayList<String> notes = new ArrayList<String>();
	
	public void add(String s) {
		notes.add(s);
		// notes.add(10)
	}
	
	public void add(String s, int location) {
		notes.add(location, s);
	}
	public int getSize() {
		return notes.size();
	}
	
	public String getNote(int index) {
		return notes.get(index);
		
	}
	
	public void removeNote(int index) {
		notes.remove(index);
	}
	
	public String[] list() {
		String[] a = new String[notes.size()];
		for (int i = 0; i < notes.size(); i++ ) {
			a[i] = notes.get(i);
		}
		return a;
		
	}
	
	public static void main(String[] args) {
		NoteBook nb = new NoteBook();
		nb.add("first");
		nb.add("second");
		nb.add("third", 1);
		System.out.println(nb.getSize());
		System.out.println(nb.getNote(0));
		System.out.println(nb.getNote(1));
		System.out.println("----------");
		String[] a = nb.list();
		for (String s : a ) {
			System.out.println(s);
		}
	}

}
