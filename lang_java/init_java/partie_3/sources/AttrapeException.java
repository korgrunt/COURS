// calcule la moyenne des entiers pass�s en ligne de commande en g�rant les non-entiers
class AttrapeException {


	static float moyenne( String[] liste ) {
		int i=0, somme=0, entier=0, nbNotes=0;
		for( i=0; i < liste.length; i++ ) try {
			entier = Integer.parseInt( liste[i] );
			somme += entier;
			nbNotes++;
		} catch( NumberFormatException e ) {
			System.out.println( "la " + (i+1) + "eme note n'est pas entiere" );
		}
		return (float)somme/nbNotes;
	}


	public static void main( String[] args ) {
		System.out.println( "la moyenne est " + moyenne( args ) );
	}


}
