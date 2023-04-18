import {Column, Entity, ManyToMany, ManyToOne, OneToMany} from "typeorm";

@Entity()
export class GenreEntity extends BaseEntity{
    @Column()
    name: string;

    @Column()
    descripition: string;

    @Column()
    image: string;

    @ManyToMany(() => MovieEntity, (movie) => movie.cast)
    moviesCast: MovieEntity[];

    @OneToMany(() => MovieEntity, (movie) => movie.director)
    moviesDirected: MovieEntity[];
}